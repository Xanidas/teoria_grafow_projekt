import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component, Renderer2, ViewChild } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Chart, ChartData, ChartOptions, registerables } from 'chart.js';
import { BaseChartDirective } from 'ng2-charts';
import { environment } from '../environments/environment';
import { firstValueFrom } from 'rxjs';

interface AlgorithmResponse {
  time: number;
  dfs_result?: {
    visited_nodes: string[];
    visited_edges: [string, string][];
  };
  bfs_result?: {
    visited_nodes: string[];
    visited_edges: [string, string][];
  };
}

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
  enableThemeSwitch = environment.enableThemeSwitch === "true";
  @ViewChild(BaseChartDirective) chart: BaseChartDirective | undefined;

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

  async buildAndSendGraph(event: Event): Promise<void> {
    event.preventDefault();

    const nodes = this.nodesInput.split(',').map((node) => node.trim());
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

    const requestBody = {
      nodes: nodes,
      edges: edges.map(([from, to]) => [from, to]),
    };

    const startNode = nodes[0];
    console.log(environment);
    try {
      const [bfsResponse, dfsResponse] = await Promise.all([
        firstValueFrom(
          this.http.post<AlgorithmResponse>(
            `${environment.apiUrl}/bfs?start_node_label=${startNode}`,
            requestBody
          )
        ),
        firstValueFrom(
          this.http.post<AlgorithmResponse>(
            `${environment.apiUrl}/dfs?start_node_label=${startNode}`,
            requestBody
          )
        ),
      ]);

      this.handleGraphResponse({
        bfs: bfsResponse.time,
        dfs: dfsResponse.time,
      });

    } catch (error) {
      console.error('Error making API calls:', error);
    }
  }

  handleGraphResponse(response: { bfs: number; dfs: number }): void {
    this.algorithmResults = response;
    this.chartData.datasets[0].data = [response.bfs];
    this.chartData.datasets[1].data = [response.dfs];
    if (this.chart) {
      this.chart.update();
    }
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
