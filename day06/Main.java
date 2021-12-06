import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        ArrayList<Integer> fish = new ArrayList<Integer>();

        fish.add(3);
        fish.add(4);
        fish.add(3);
        fish.add(1);
        fish.add(2);

        System.out.println("fish:" + fish);
        System.out.println("len:" + fish.size());

        for (int i=1; i<=256; i++) {
            process(fish);
            System.out.println("day "+i+" - len:" + fish.size());
        }

        System.out.println("len:" + fish.size());

    }

    private static void process(List<Integer> fish) {
        int countSpawn = 0;
        for(int j=0; j < fish.size(); j++) {
            int val = fish.get(j);
            if(val==0) {
                fish.set(j, 6);
                countSpawn += 1;
            } else {
                fish.set(j, val-1);
            }
        }
        for(int j=0; j < countSpawn; j++) {
            fish.add(8);
        }
        //System.out.println("fish:" + fish);
        //System.out.println("len:" + fish.size());
    }

}