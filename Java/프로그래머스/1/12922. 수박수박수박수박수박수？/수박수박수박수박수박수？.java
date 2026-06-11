import java.util.*;
import java.io.*;

class Solution {
    public String solution(int n) {
        String answer = "";
        StringBuilder sb = new StringBuilder(answer);
        
        String su = "수";
        String bak = "박";
        
        if(n % 2 == 0) {
            for(int i=0; i<n/2; i++) {
                sb.append(su);
                sb.append(bak);
            }
            
        }
        else {
            for(int i=0; i<n; i++) {
                if(i % 2 == 0) {
                    sb.append(su);
                }
                else {
                    sb.append(bak);
                }
            }
        }
        return sb.toString();
    }
}