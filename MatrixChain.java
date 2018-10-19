public class MatrixChain {
       public String printOp(int i, int j, int[][] sp) {
                if (i == j) {
			return "A" + String.valueOf(i + 1);
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
				System.out.print(String.valueOf(dp[i][j]) + " ");
			}
			System.out.println();
		}
		System.out.println();
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				System.out.print(String.valueOf(sp[i][j]) + " ");
			}
			System.out.println();
		}

		if (n == 0){
			System.out.println("(A1)");
		} else {
			System.out.println(this.printOp(0, n-1, sp));		
		}
	}
	
	public static void main(String[] args) {
		int[] test = { 30,35,15,5,10,20,25 };
		(new MatrixChain()).multiplyOrder(test);
	}
}
