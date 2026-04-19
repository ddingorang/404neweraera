import java.util.*;
import java.io.*;

public class Main {
    static int M, N;
    static int[][] map, dp;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        map = new int[M][N];
        dp = new int[M][N];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                dp[i][j] = -1; // 방문하지 않은 상태를 -1로 초기화
            }
        }

        System.out.println(dfs(0, 0));
    }

    static int dfs(int x, int y) {
        // 목적지에 도착하면 경로 1개 발견
        if (x == M - 1 && y == N - 1) return 1;

        // 이미 계산된 적이 있다면 그 값을 즉시 반환
        if (dp[x][y] != -1) return dp[x][y];

        dp[x][y] = 0; // 방문 처리 (경로 탐색 시작)
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < M && ny >= 0 && ny < N && map[nx][ny] < map[x][y]) {
                dp[x][y] += dfs(nx, ny);
            }
        }
        return dp[x][y];
    }
}