package dateTime;

import java.time.LocalTime;

public class CurrentTime {

	public static void main(String[] args) {
		LocalTime currentTime = LocalTime.now();
		System.out.println(currentTime);
	}

}
