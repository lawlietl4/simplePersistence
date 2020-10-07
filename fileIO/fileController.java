package src.fileIO;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.stream.Stream;

public class fileController {
    final static File simpleFolder = new File("..\\databasesjava1\\Assignment 1 - data\\simple\\");
    final static File longFolder = new File("..\\databasesjava1\\Assignment 1 - data\\long\\");
    public static void run(){
        PrintEmployees(simpleFolder);
    }
    public static void mainMenu(){
        boolean isValid;
        String input;
        String menu = "\n\nWelcome to the employee folder file editor\n"
                + "1)read short folder\n"
                + "2)";
    }
    public static void PrintPeopleDetails(final File path){
        String line;
        BufferedReader buffy;
        try (Stream<Path> paths = Files.walk(Paths.get("..\\databasesjava1\\Assignment 1 - data\\simple\\"))){
            for (int i = 1; i<path.listFiles().length; i++) {
                FileReader fr = new FileReader("..\\databasesjava1\\Assignment 1 - data\\simple\\" +i+".txt");
                buffy = new BufferedReader(fr);
                while((line = buffy.readLine())!=null){
                    System.out.println(line);
                }
                fr.close();
            }
        }
        catch(IOException ioe){
            ioe.printStackTrace();
        }
    }
    public static void PrintEmployees(final File path){
        String line;
        BufferedReader buffy;
        try (Stream<Path> paths = Files.walk(Paths.get("..\\databasesjava1\\Assignment 1 - data\\simple\\"))){
            for (int i = 1; i<path.listFiles().length; i++) {
                FileReader fr = new FileReader("..\\databasesjava1\\Assignment 1 - data\\simple\\" + i +".txt");
                buffy = new BufferedReader(fr);
                while((line = buffy.readLine())!=null){
                    System.out.println(line);
                }
                Files.lines(simpleFolder.toPath()).map(s -> s.trim()).filter(s -> !s.matches("[1-9]")).forEach(System.out::println);
                fr.close();
            }
        }

        catch(IOException ioe){
            ioe.printStackTrace();
        }
    }
}
