
function escapeHtml(text) {
    return $('<div>').text(text).html();
}

function generateFlagTableRows(rows,sploits) {
    var html = '<thead><tr class="table-secondary"><td>Teams </td>';
    sploits.forEach(s => {
        html += '<td>' + escapeHtml(s) + '</td>';
    });
    html += '<td id="total">Total</td></tr></thead><tbody>';    
    rows.forEach(row => {
        html += '<tr>';
        row.forEach(function (text) {
            html += '<td>' + escapeHtml(text) + '</td>';
        });
        html += '</tr>';
    });
    html += '</tbody>;'
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
                coloumns = [];
                sploits.forEach(s => 
                    coloumns.push(flags.filter(f => f.team == t && f.sploit == s ).length)
                 );
                 coloumns.push(coloumns.reduce((total,v) => total + v ));
                 coloumns.unshift(t);
                rows.push(coloumns);
            });
            
            $('#flag-table').html(generateFlagTableRows(rows,sploits));
            sorttable.makeSortable(document.getElementById('flag-table'));
            sorttable.innerSortFunction.apply(document.getElementById('total'), []);
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
    showFlags();
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
