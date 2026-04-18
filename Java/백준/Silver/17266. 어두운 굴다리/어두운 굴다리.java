import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        List<Integer> location = new ArrayList<>();

        location.add(0); // 시점
        for(int i = 0; i<m; i++) {
            location.add(Integer.parseInt(st.nextToken()));
        }
        location.add(n); // 종점

        int front = location.get(1); // 첫 가로등과 시점 사이 거리
        int back = location.get(m+1) - location.get(m); // 종점과 마지막 가로등 사이 거리

        int max = 0;
        for(int j = 0; j<m+1; j++) {
            if(location.get(j+1) - location.get(j) > max) {
                max = location.get(j+1) - location.get(j);
                // 시점 - 종점 사이 가로등간 거리가 최대일 때의 거리 얻기
            }
        }
        
        // 두 가로등이 반씩 영역을 커버해아 함
        int afterdiv = 0;
        if (max % 2 == 0) {
             afterdiv = max / 2;
        }
        else {
            afterdiv = (int)(Math.ceil((double) max / 2));
        }

        // 가로등과 가로등 사이는 두 가로등이 반씩 커버할 수 있지만
        // 시점과 종점에는 가로등이 없어 하나의 가로등이 커버를 해야 함
        if(front >= afterdiv) {
            System.out.println(front);
        }
        else if(back >= afterdiv) {
            System.out.println(back);
        }
        else {
            System.out.println(afterdiv);
        }

    }
}