import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component, Renderer2 } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Chart, ChartData, ChartOptions, registerables } from 'chart.js';
import { BaseChartDirective } from 'ng2-charts';
import { environment } from '../environments/environment';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [FormsModule, CommonModule, BaseChartDirective],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  nodesInput = '';
  edgesInput = '';
  graphJson: { [key: string]: string[] } | null = null;
  algorithmResults: { [key: string]: number } = {};
  enableThemeSwitch = environment.enableThemeSwitch;

  chartData: ChartData<'bar'> = {
    labels: ['Czas wykonywania'],
    datasets: [
      {
        label: 'BFS',
        data: [0.02],
        backgroundColor: 'rgba(163, 227, 140, 0.6)',
        borderColor: 'rgba(163, 227, 140, 1)',
        borderWidth: 1,
      },
      {
        label: 'DFS',
        data: [0.04],
        backgroundColor: 'rgba(113, 159, 173, 0.6)',
        borderColor: 'rgba(113, 159, 173, 1)',
        borderWidth: 1,
      },
    ],
  };

  chartOptions: ChartOptions = {
    responsive: true,
    indexAxis: 'y',
    scales: {
      x: {
        min: 0,
        beginAtZero: true,
      },
    },
  };

  constructor(private http: HttpClient, private renderer: Renderer2) {
    Chart.register(...registerables);
  }

  buildAndSendGraph(event: Event): void {
    event.preventDefault();

    // Parse nodes
    const nodes = this.nodesInput.split(',').map((node) => node.trim());

    // Parse edges
    const edges = this.edgesInput
      .split(',')
      .map((edge) => edge.trim().split('-'));

    // Build graph JSON
    const graph: { [key: string]: string[] } = {};
    nodes.forEach((node) => (graph[node] = []));
    edges.forEach(([from, to]) => {
      if (graph[from]) graph[from].push(to);
      if (graph[to]) graph[to].push(from);
    });

    this.graphJson = graph;
    const mockResponse = {
      bfs: 0.02,
      dfs: 0.04,
    };

    // Simulate the API call response with the mock data
    this.handleGraphResponse(mockResponse);
  }

  handleGraphResponse(response: { bfs: number; dfs: number }): void {
    console.log('Mock response:', response);
    this.algorithmResults = response;
    // Update the chart with the response data (BFS and DFS times)
    this.chartData.datasets[0].data = [response.bfs, response.dfs];
  }

  toggleTheme(event: Event): void {
    const isChecked = (event.target as HTMLInputElement).checked;

    if (isChecked) {
      this.renderer.addClass(document.body, 'dark-mode');
    } else {
      this.renderer.removeClass(document.body, 'dark-mode');
    }
  }
}
