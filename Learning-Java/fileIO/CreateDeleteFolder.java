package fileIO;

import java.io.File;

public class CreateDeleteFolder {

	public static void main(String[] args) {
		//createFolder("test");
		//deleteFolder("test");
	}
	
	public static void createFolder(String foldername) {
		File f = new File(foldername);
		if(f.mkdir()) {
			System.out.println("Created Folder!");
		}
		else {
			System.out.println("Failed to create folder!");
		}
	}
	
	public static void deleteFolder(String foldername) {
		File f = new File(foldername);
		if(f.delete()) {
			System.out.println("Deleted Folder!");
		}
		else {
			System.out.println("Failed to delete folder!");
		}
	}
}
