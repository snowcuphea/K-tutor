<template>
  <div>
    <canvas id="grade-chart" height="200"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js'

export default {
  name: 'GradeChart',
  data() {
    return {
      gradeChart: {
        type: "line",
        data: {
          labels: this.$store.state.userGrade.dates,
          datasets: [
            {
              label: "Grades",
              data: this.$store.state.userGrade.grades,
              backgroundColor: "rgba(0,0,0,0)",
              borderColor: "#36495d",
              borderWidth: 3,
              pointRadius:5,
              pointHoverRadius:5,
              pointBorderColor: "#36495d",
              pointBackgroundColor: "#36495d"
            },
          ]
        },
        options: {
          title: {
            display: true,
            text: "Last 10 test grades",
            fontSize: 16,
          },
          tooltips:{
            callbacks: {
              label: function(tooltipItem) {
                console.log(tooltipItem)
                return String(tooltipItem.xLabel) + Number(tooltipItem.value)
              }
            }
          },
          legend: {
            display: false
          },
          responsive: true,
          lineTension: 0,
          scales: {
            yAxes: [
              { 
                ticks: {
                  beginAtZero: true,
                  suggestedMax: 100,
                  stepSize: 20,
                  padding: 0
                }
              }
            ],
            xAxes: [
              {
                scaleLabel: {
                  display: true,
                  labelString: 'date (M/D)'
                }
              }
            ]
          }
        }
      }
    }
  },
  mounted() {
    const ctx = document.getElementById('grade-chart')
    new Chart(ctx, this.gradeChart)
  },
}
</script>

<style>

</style>