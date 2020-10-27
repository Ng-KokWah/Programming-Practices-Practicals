/*
 * enum/enumerations (meaning specifically listed)
 * is a special class that represents a group of constants (like final variables)
 */
public class Enums {
	enum Level {
		LOW,
		MEDIUM,
		HIGH
	}
	
	public static void main(String[] args) {
		//to access the enum -> Level var = Level.MEDIUM
		Level myVar = Level.MEDIUM; 
	    System.out.println(myVar); //MEDIUM
	    
	    //to loop through all enum constants
	    for (Level myVar2 : Level.values()) {
	    	System.out.println(myVar2);
	    }
	}
}
