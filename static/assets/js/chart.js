let ctx = document.getElementById('myChart').getContext('2d');
let labels = ['Negative', 'Positive', 'Neutral'];
let colorHex = [ '#EFCA08','#FB3640', '#43AA8B'];
var neg_data = document.getElementById('var1').value*100
var pos_data = document.getElementById('var2').value*100
var neu_data = document.getElementById('var3').value*100

let myChart = new Chart(ctx, {
  type: 'pie',
  data: {
    datasets: [{
      data: [neg_data,pos_data,neu_data],
      backgroundColor: colorHex
    }],
    labels: labels
  },
  options: {
    responsive: true,
    legend: {
      position: 'bottom'
    },
    plugins: {
      datalabels: {
        color: '#fff',
        anchor: 'end',
        align: 'start',
        offset: -10,
        borderWidth: 2,
        borderColor: '#fff',
        borderRadius: 25,
        backgroundColor: (context) => {
          return context.dataset.backgroundColor;
        },
        font: {
          weight: 'bold',
          size: '10'
        },
        formatter: (value) => {
          return value + ' %';
        }
      }
    }
  }
})