<template>
  <div>
    <canvas id="grade-chart" height="200"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js'
import { mapState } from 'vuex'


export default {
  name: 'GradeChart',
  data() {
    return {
      gradeChart: {
        type: "line",
        data: {
          labels: this.$store.state.userGrade_date,
          datasets: [
            {
              label: "Grades",
              data: this.$store.state.userGrade_score,
              backgroundColor: "rgba(0,0,0,0)",
              borderColor: "#00bfa5",
              borderWidth: 3,
              pointRadius:5,
              pointHoverRadius:5,
              pointBorderColor: "#00bfa5",
              pointBackgroundColor: "#00bfa5"
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
            displayColors: false,
            titleAlign: "center",
            callbacks: {
              title: function(tooltipItem) {
                const date = tooltipItem[0].xLabel.split('T')
                const ymd = date[0][5]+date[0][6] + "/" + date[0][8]+date[0][9] + "/" + date[0][2]+date[0][3]
                const time = date[1][0]+date[1][1] + ":" + date[1][3] + date[1][4]
                return ymd + " " + time
              },
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
                },
                ticks: {
                  callback(data) {
                    return data[5]+data[6] + "/" + data[8]+data[9]
                  }
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
  created() {
  },
  computed: {
    ...mapState(["userGrade_date", "userGrade_score" ])
  },
  watch: {
    userGrade_date() {
      this.gradeChart.data.labels = this.userGrade_date
      this.gradeChart.data.datasets[0].data = this.userGrade_score
      const ctx = document.getElementById('grade-chart')
      new Chart(ctx, this.gradeChart)
    }
  }
}
</script>

<style>

</style>