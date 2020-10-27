import java.util.ArrayList;
import java.util.Iterator;

public class IteratorObj {
	/*
	 * An iterator is an object that is used to loop through collections
	 * like arraylist or hashsets, etc
	 * 
	 * this is usually used to easily and quickly remove items while looping through a collection
	 */
	public static void main(String[] args) {
		// Make a collection
	    ArrayList<String> cars = new ArrayList<String>();
	    cars.add("Volvo");
	    cars.add("BMW");
	    cars.add("Ford");
	    cars.add("Mazda");
	    System.out.println(cars);

	    // Get the iterator
	    Iterator<String> it = cars.iterator();

	    // Print the first item
	    System.out.println(it.next());
	    
	    //loop through a collection and remove BMW
	    while(it.hasNext()) {
	    	String i = it.next();
	    	if(i == "BMW") {
	    		it.remove();
	    	}
	    }
	    
	    System.out.println(cars);
	}

}
