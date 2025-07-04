/*import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);


const ctx = document.getElementById('myChart') as HTMLCanvasElement

//この2つの値を設定するだけ!!
const percentage = 76 //グラフのパーセンテージ(76%)
const backgroundColor = 'rgba(255, 0, 0, 1)' //グラフの色(赤)

new Chart(ctx, {
  type: 'doughnut',
  data: {
    datasets: [{
      data: [percentage, 100 - percentage],
      backgroundColor: [
        backgroundColor, //赤色
        'rgba(0, 0, 0, 0)',
      ],
      borderWidth: 0
    }]
  }
})
*/
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);

window.addEventListener('load', () => {
  const canvas = document.getElementById('myChart') as HTMLCanvasElement;
  const ctx = canvas.getContext('2d');

  const percentage = 76;
  const backgroundColor = 'rgba(255, 0, 0, 1)';

  if (ctx) {
    new Chart(ctx, {
      type: 'doughnut',
      data: {
        datasets: [{
          data: [percentage, 100 - percentage],
          backgroundColor: [
            backgroundColor,
            'rgba(0, 0, 0, 0)'
          ],
          borderWidth: 0
        }]
      },
      options: {
        cutout: '70%',
        plugins: {
          legend: { display: false },
          tooltip: { enabled: false }
        }
      }
    });
  } else {
    console.error('ctx is null: Canvas not found or not ready');
  }
});

