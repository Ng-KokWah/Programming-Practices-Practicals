package dateTime;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class CurrentDateNTime {

	public static void main(String[] args) {
		LocalDateTime datetime = LocalDateTime.now();
		System.out.println("Before Format: " + datetime);
		
		/*
		 * yyyy-MM-dd	"1988-09-29"	
			dd/MM/yyyy	"29/09/1988"	
			dd-MMM-yyyy	"29-Sep-1988"	
			E, MMM dd yyyy	"Thu, Sep 29 1988"
		 */
		DateTimeFormatter format = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
		String formattedDT = datetime.format(format);
		System.out.println("After Format: " + formattedDT);
	}

}
