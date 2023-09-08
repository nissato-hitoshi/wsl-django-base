
var items = ''

$(function() {
    $("#keyword").on(
        "input", 
        async function() {

            var v = $(this).val();
            const result = document.getElementById('result');
            result.innerHTML = ''

            if (v) { 
                await fetch('/api/1.0/employees/?search=' + v)
                    .then((res) => {
                            return res.json()
                        })
                    .then((json) => {
                        items = json
                        out = '<table class="table table-striped table-hover table-sm">'
                        out = out + '<tbody>'
                        for (var i=0; i < json.length; i++) {
                            out = out + "<tr onclick='select_item(" + i + ")' style='cursor:pointer'>"
                            out = out + "<td>" + json[i].employee_no + "</td>";
                            out = out + "<td>" + json[i].name + "</td>";
                            out = out + "<td>" + json[i].email + "</td>";
                            out = out + "</tr>"
                        }
                        out = out + '</tbody>'
                        out = out + "</table>"

                        result.innerHTML = out
                    });
            }
        }
    )
})

function select_item(index) {
    target = document.getElementById('keyword')
    target.value = items[index].name
    target = document.getElementById('result')
    target.innerHTML = ''
}