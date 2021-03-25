<template>
  <div>
    <canvas id="grade-chart"></canvas>
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
          labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
          datasets: [
            {
              label: "Grades",
              data: this.$store.state.userGrade,
              backgroundColor: "rgba(0,0,0,0)",
              borderColor: "#36495d",
              borderWidth: 3
            },
          ]
        },
        options: {
          responsive: true,
          lineTension: 0,
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true,
                  padding: 0
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