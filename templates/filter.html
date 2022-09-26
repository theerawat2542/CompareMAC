<!DOCTYPE html>
<html>
<head>
    <title>Report</title>
    <style>
        .topright {
          position: absolute;
          top: 8px;
          right: 16px;
          font-size: 18px;
        }
    </style>
<script>
    function exportTableToExcel(tableID, filename = ''){
    var downloadLink;
    var dataType = 'application/vnd.ms-excel';
    var tableSelect = document.getElementById(tableID);
    var tableHTML = tableSelect.outerHTML.replace(/ /g, '%20');
    
    // Specify file name
    filename = filename?filename+'.xls':'excel_data.xls';
    
    // Create download link element
    downloadLink = document.createElement("a");
    
    document.body.appendChild(downloadLink);
    
    if(navigator.msSaveOrOpenBlob){
        var blob = new Blob(['\ufeff', tableHTML], {
            type: dataType
        });
        navigator.msSaveOrOpenBlob( blob, filename);
    }else{
        // Create a link to the file
        downloadLink.href = 'data:' + dataType + ', ' + tableHTML;
    
        // Setting the file name
        downloadLink.download = filename;
        
        //triggering the function
        downloadLink.click();
    }
}
</script>
</head>
<body>

<b>{{rows}} Records Found</b>

<table class="table table-striped custab" id="tblData">
    <thread>
        <td><b>Date/Time</b></td>
        <td><b>Product Code</b></td>
        <td><b>Mac Address</b></td>
        <td><b>Test Result</b></td>
    </thread>
    {% for row in db %}
    <tr>
        <td>{{row.date_time}}</td>
        <td>{{row.product_code}}</td>
        <td>{{row.mac_address}}</td>
        <td>{{row.result}}</td>
    </tr>
    {% endfor %}
</table>

<button onclick="exportTableToExcel('tblData', 'report-data')" style="background-color:green; color:white;">Excel File</button>

<!--<button id="downloadexcel" class="topright">Export to Excel</button>-->

</body>
</html>