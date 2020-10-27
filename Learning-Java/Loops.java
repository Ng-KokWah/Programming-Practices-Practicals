
public class Loops {
	public static void main(String[] args) {
		
		//for loop
		for(int i=0; i<=10; i++) {
			System.out.println("For Loop: " + i);
		}
		
		//do while loop -> does the loop at least once, like for this case even though j is < 1 it would still
		//print Do While Loop: 0, even though the condition is already completed
		int j=0;
		do {
			System.out.println("Do While Loop:" + j);
			j++;
		}while(j < 1);
		
		//while loop
		int k=0;
		while(k < 10) {
			System.out.println("While loop: " + k);
			k++;
		}
	}
}
