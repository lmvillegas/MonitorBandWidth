let draw = false;

init();

/**
 * FUNCTIONS
 */

function init() {
  // initialize DataTables
  const table = $("#datatable-basic").DataTable();
  // get table data
  const tableData = getTableData(table);
   // create Highcharts
  createCharts(tableData);
  setTableEvents(table);
}



function getTableData(table) {
  const dataArray = [],
    indexArray = [],
    timestampArray = [],
    pingArray = [],
    downloadArray = [],
    uploadArray = [];

  // loop table rows

  table.rows({search: "applied"}).every(function () {
    const data = this.data();
    indexArray.push(data[0]);
    timestampArray.push(data[1]);
    pingArray.push(data[2]);
    downloadArray.push(data[3]);
    uploadArray.push(data[4]);;
  });

  // store all data in dataArray
  dataArray.push(timestampArray, downloadArray, uploadArray);

  return dataArray;
}

function createCharts(data) {
  var timeFormat = 'YYYY/MM/DD HH:mm';
  var ctx = document.getElementById("canvas").getContext("2d");
  var canvas = new Chart(ctx, {
    type: 'line',
    data: {
      labels: data[0],
      datasets: [
        {
          label: "Descarga de Ancho de Banda en MB",
          backgroundColor: window.chartColors.red,
          borderColor: window.chartColors.red,
          fill: false,
          data: data[1],
          yAxisID: 'y-axis-1'
        },
        {
          label: "Carga de Ancho de Banda en MB",
          backgroundColor: window.chartColors.blue,
          borderColor: window.chartColors.blue,
          fill: false,
          data: data[2],
          yAxisID: 'y-axis-2'
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Monitor de Ancho de banda'
      },
      scales: {
        yAxes: [{
          display: true,
          position: 'left',
          id: 'y-axis-1',
        }, {
          display: true,
          position: 'right',
          id: 'y-axis-2',

          // grid line settings
          gridLines: {
            drawOnChartArea: false, // only want the grid lines for one axis to show up
          },
         }],
      }
    }
  });
}

function setTableEvents(Tarray) {
  // listen for page clicks
  table.on("page", () => {
    draw = true;
  });

  // listen for updates and adjust the chart accordingly
  table.on("draw", () => {
    if (draw) {
      draw = false;
    } else {
      const tableData = getTableData(table);
      createCharts(tableData);
      // table events
    }
  });
}