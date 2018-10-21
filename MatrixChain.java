public class MatrixChain {
       public String printOp(int i, int j, int[][] sp) {
                if (i == j) {
			return "A" + String.valueOf(i);
		} else {
			return "(" + this.printOp(i, sp[i][j], sp) + "x" + this.printOp(sp[i][j] + 1, j, sp) + ")";
		}
       }

       public void multiplyOrder(int[] p) {
		int n = p.length - 1;
		int[][] dp = new int[n + 1][n + 1];
		int[][] sp = new int[n + 1][n + 1];
	
		for (int l = 2; l <= n; l++) {
			for (int i = 1; i <= n - l + 1; i++) {
				int j = i + l - 1;
				dp[i][j] = Integer.MAX_VALUE;
				for (int k = i; k <= j - 1; k++) {
					int tmp = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j];
					if (tmp < dp[i][j]){
						dp[i][j] = tmp;
						sp[i][j] = k;
					}
				}
			}
		}
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				System.out.printf("%6d ",dp[i][j]);
			}
			System.out.println();
		}
		System.out.println();
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				System.out.printf("%6d ", sp[i][j]);
			}
			System.out.println();
		}

		if (n == 0){
			System.out.println("(A1)");
		} else {
			System.out.println(this.printOp(1, n, sp));
		}
	}
	
	public static void main(String[] args) {
		int[] test = { 10,20,50,1,100 }; // ((M1*(M2*M3))*M4)
		//int[] test = { 10,20,5,4,30,6 }; // ((M1*M2)*(M3*(M4*M5)))
		//int[] test = { 30,35,15,5,10,20,25 }; // ((M1*(M2*M3))*((M4*M5)*M6))
		(new MatrixChain()).multiplyOrder(test);
	}
}
