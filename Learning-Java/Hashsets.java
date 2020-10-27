import java.util.HashSet;

public class Hashsets {
	public static void main(String[] args) {
		//hash set is a collection of items where every item is unique
		//especially useful if you dont want to allow the addition of duplicate items
		HashSet<String> cars = new HashSet<String>();
		//add items
		cars.add("Volvo");
	    cars.add("BMW");
	    cars.add("Ford");
	    cars.add("BMW");
	    cars.add("Mazda");
	    System.out.println(cars);
	    //NOTE: even though BMW is added twice, when printed only one appears in the set
	    
	    //check if item exists
	    System.out.println(cars.contains("Mazda"));
	    
	    //to check how many items there are
	    System.out.println(cars.size());
	    
	    //to loop through the items
	    for (String i : cars) {
	    	System.out.println(i);
	    }
	    
	    //remove item
	    cars.remove("Volvo");
	    System.out.println(cars);
	    
	    //remove all items
	    cars.clear();
	    
	}
}
