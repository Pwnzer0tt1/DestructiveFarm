
function escapeHtml(text) {
    return $('<div>').text(text).html();
}

function generateFlagTableRows(rows,sploits) {
    var html = '<tr class="table-secondary"><td>Teams </td>';
    sploits.forEach(s => {
        html += '<td>' + escapeHtml(s) + '</td>';
    });
    html += '</tr>';    
    rows.forEach(row => {
        html += '<tr>';
        row.forEach(function (text) {
            html += '<td>' + escapeHtml(text) + '</td>';
        });
        html += '</tr>';
    });
    return html;
}

var queryInProgress = false;

function showFlags() {
    if (queryInProgress)
        return;
    queryInProgress = true;

    $('.search-results').hide();
    $('.query-status').html('Loading...').show();

    $.get('/ui/show_team_exploit', { 'tick' : document.getElementById("tick-input").value})
        .done(function (response) {
            teams = response.distinct_values['team'];
            sploits = response.distinct_values['sploit'];
            flags = response.flags;
            rows = [];
            teams.forEach(t => {
                coloumns = [t]
                sploits.forEach(s => 
                    coloumns.push(flags.filter(f => f.team == t && f.sploit == s ).length)
                 );
                rows.push(coloumns);
            });
            
            console.log(rows);

            $('.search-results tbody').html(generateFlagTableRows(rows,sploits));
            $('.query-status').hide();
            $('.search-results').show();
        })
        .fail(function () {
            $('.query-status').html("Failed to load flags from the farm server");
        })
        .always(function () {
            queryInProgress = false;
        });
}

$(function () {
    $('#show-flags-form').submit(function (event) {
        event.preventDefault();
        showFlags();
    });

    var slider = document.getElementById("tick-input");
    var output = document.getElementById("submit-btn");
    output.innerHTML = "Show #" + slider.value; // Display the default slider value
    
    // Update the current slider value (each time you drag the slider handle)
    slider.oninput = function() {
      output.innerHTML = "Show #" + this.value;
    } 
});
