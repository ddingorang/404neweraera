import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int[][] map, dp;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new int[N][N];
        dp = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int maxDays = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                maxDays = Math.max(maxDays, dfs(i, j));
            }
        }
        System.out.println(maxDays);
    }

    static int dfs(int x, int y) {
        // 이미 계산된 경로라면 반환
        if (dp[x][y] != 0) return dp[x][y];

        // 기본적으로 현재 칸은 1만큼의 경로를 가짐
        dp[x][y] = 1;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            // 범위 안이고, 다음 칸의 값이 현재 칸보다 크다면
            if (nx >= 0 && nx < N && ny >= 0 && ny < N && map[nx][ny] > map[x][y]) {
                dp[x][y] = Math.max(dp[x][y], dfs(nx, ny) + 1);
            }
        }
        return dp[x][y];
    }
}