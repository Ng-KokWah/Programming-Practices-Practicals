package fileIO;

import java.io.FileWriter;
import java.io.IOException;

public class WriteToFile {

	public static void main(String[] args) {
		try {
			FileWriter writer = new FileWriter("test.txt");
			writer.write("testing 1,2,3");
			writer.close();
			System.out.println("Wrote to file!");
		}catch(IOException e) {
			e.printStackTrace();
		}
	}

}
