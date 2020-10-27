import java.util.HashMap;

public class HashMapObj {
	public static void main(String[] args) {
		/*
		 * Unlike arrays, which store items in an ordered collection
		 * Hashmaps stores items in key-value pairs
		 */
		// Create a HashMap object called capitalCities
		//the data type for either the key or the value that the hashmap can accept can be changed to 
		//HashMap<String, Integer>, which in terms means that the key is a string and the value is a integer
		//e.g. people.put("John", 40);
	    HashMap<String, String> capitalCities = new HashMap<String, String>();

	    // Add keys and values (Country, City)
	    capitalCities.put("England", "London");
	    capitalCities.put("Germany", "Berlin");
	    capitalCities.put("Norway", "Oslo");
	    capitalCities.put("USA", "Washington DC");
	    System.out.println(capitalCities);
	    
	    //to access an item
	    System.out.println(capitalCities.get("England"));
	    
	    //find out how many items there are
	    System.out.println(capitalCities.size());
	    
	    //remove an item
	    capitalCities.remove("England");
	    System.out.println(capitalCities);
	    
	    //to remove all items
	    capitalCities.clear();
	    System.out.println(capitalCities);
	    
	    // Print keys with the .keySet() and if you want to print the values use .values()
	    // Print both keys and values
	    for (String i : capitalCities.keySet()) {
	      System.out.println("key: " + i + " value: " + capitalCities.get(i));
	    }
	    
	    
	}
}
