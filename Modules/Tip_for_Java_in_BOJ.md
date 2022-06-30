1. 클래스명은 Main
2. 패키지 X
3. Main 이외의 클래스를 추가로 사용하려면 public 아닌 클래스 or Inner 클래스 사용
4. solution 함수로 래핑해서 사용하면 편리 
    * main 함수에서 바로 작성 시, main 함수가 static이므로 main에서 사용하는 전역 변수 및 모든 함수가 static이어야 한다.
```java
public class Main {
   private int max = 0;
   private int n, k;
   private int[] arr;
   
   private void dfs(int cnt, int num){
     if(cnt==8){
       return;
     }
     num += 10;
     if(nnum>=n){
       return;
     }
     
     for(int i=0; i < k; i++){
       int tmp = num + arr[i];
       if (tmp > n) continue;
       if (tmp > max) max = tmp;
       dfs(cnt+1, tmp);
     }
   }
 
   public void solution() throws Exception{
     BufferdReader br = new BufferedReader(new InputStreamReader(System.in));
     StringTokenizer st = new StringTokenizer(br.readLine());
     n = Integer.parseInt(st.nextToken());
     k = Integer.parseInt(st.nextToken());
     arr = new int[k];
     st = new StringTokenizer(br.readLine());
     for(int i=0;i<k;i++) arr[i] = Integer.parseInt(st.nextToken());
     
     dfs(0, 0);
     System.out.println(max);
   }
   public static void main(String[] args) throws Exception {
     new Main().solution();
   }
 }
```
5. 빠르게 입력 받기 위해 BufferedReader, StringTokenizer 사용
    * 일반적으로 `Scanner sc = new Scanner(System.in);`으로 입력 받곤 하지만 느리다(Scanner내부에서 nextFloat() 호출 시 다음 입력을 찾기 위해 정규식 사용하기 때문)
    * String에 대한 split() 보다는 StringTokenizer가 빠르다.
    ```java
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n  = Integer.parseInt(br.readLine());
    for(int i = 0; i < n; i++){
      StringTokenizer st = new StringTokenizer(br.readLine());
      int s = Integer.parseInt(st.nextToken());
      
      for(int j = 0; j < s; j++){
        int data = Integer.parseInt(st.nextToken());
        System.out.println(data);
      }
    }
    ```
 6. 출력도 느린 System.out.println() 대신 BufferedWriter
 ```java
  BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

      for(int j = 0; j < s; j++){
        int data = Integer.parseInt(st.nextToken());
        bw.write(String.valueOf(data));
        bw.newLine();
        
   bw.flush();
```
* int를 바로 출력할 수 없어서 String.valueOf를 써야 한다.(String의 + 연산은 느림)
* 다른 방법으로는 StringBuilder로 출력할 것을 모아서 System.out.println() 사용

 ```java
  BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  StringBuilder sb = new StringBuilder();

      for(int j = 0; j < s; j++){
        int data = Integer.parseInt(st.nextToken());
        sb.append(data).append('\n');
        
   System.out.println(sb);
```
 
 
 Reference
 * https://nahwasa.com/entry/%EC%9E%90%EB%B0%94%EB%A1%9C-%EB%B0%B1%EC%A4%80-%ED%92%80-%EB%95%8C%EC%9D%98-%ED%8C%81-%EB%B0%8F-%EC%A3%BC%EC%9D%98%EC%A0%90-boj-java
