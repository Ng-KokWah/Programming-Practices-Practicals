import java.util.*;

public class ArraysNArraylist {
	public static void main(String[] args) {
		//NOTE: index of any array always start with 0
		String[] arr = {"Apple", "Orange", "Pear"};
		int[][] twoDArr = {{1, 2, 3}, {4, 5, 6}};
		//arraylist is more dynamic in terms of size
		ArrayList<String> arrList = new ArrayList<String>();
		arrList.add("Fruits");
		arrList.add("Vegetables");
		arrList.add("Electronics");
		
		//accessing all the array elements
		for(int i=0; i<arr.length; i++) {
			System.out.println("In the array Using For loop: " + arr[i]);
		}
		//OR accessing all array elements using for each loop
		for(String n:arr) {
			System.out.println("For each array: " + n);
		}
		
		//getting a specific element in the array
		String arrEle = arr[0];
		System.out.println(arrEle);
		
		//accessing all the 2d array element
		for(int row=0; row<twoDArr.length; row++) {
			for(int col=0; col<twoDArr[row].length; col++) {
				System.out.println("In the 2D Array: " + twoDArr[row][col]);
			}
		}
		
		//getting a specific element in the array
		String twoDArrEle = Integer.toString(twoDArr[0][0]);
		System.out.println(twoDArrEle);
		
		//accessing all elements in the arraylist
		for(int j=0; j<arrList.size(); j++) {
			System.out.println(arrList.get(j));
		}
		
		//getting a specific element in the arraylist
		String arrListEle = arrList.get(0);
		System.out.println(arrListEle);
		
		//searching for the index of an element
		int whereIsIt = arrList.indexOf("Electronics");
		System.out.println(whereIsIt);
		
		//to change an element in the arraylist
		arrList.set(0, "Portable");
		System.out.println(arrList);
		
		//to remove an element in the arraylist
		arrList.remove(0);
		System.out.println(arrList);
		
		//to completely remove everything from the arraylist
		arrList.clear();
		System.out.println(arrList);
	}
}
