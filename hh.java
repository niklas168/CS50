import java.util.Random;
import java.util.Scanner;

public class Lotto{
    public static void main (String[] args){

        int[] tipp = new int[6];

        Scanner input = new Scanner(System.in);


        for (int i = 0; i<6;i++){
            System.out.printf("Ihr Tipp: ");
            int guess = input.nextInt();

            if(guess>0 && guess<50){

                for (int k=0;i>6;k++){
                    if (tipp[k]==guess){
                        System.out.printf("Die Zahl kam schon einmal im Tipp vor!");
                        guess = input.nextInt();
                        k=0;
                    }
                    else
                    tipp[i]=guess;
                }

            }
            else{
            System.out.printf("Bitte eine Zahl zwischen 1 und 49 abgegeben!");
            i--;
            }

        }

    }
}

