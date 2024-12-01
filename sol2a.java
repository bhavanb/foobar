import java.util.Arrays;
import java.util.Comparator;

public class sol2a {
    static Comparator<int[]> comp = new Comparator<int[]>() {
        @Override
        public int compare(int[] a, int[] b) {
            for (int i = 0; i < a.length; i++) {
                int comparison = Integer.compare(a[i], b[i]);
                if (comparison != 0) {
                    return comparison;
                }
            }

            return Integer.compare(a.length, b.length);
        }
    };

    public static String[] solution(String[] l) {
        int[][] split = new int[l.length][3];
        String[] out = new String[l.length];

        for (int i = 0; i < l.length; i++) {
            while (l[i].split("\\.").length < 3) {
                l[i] += ".-1";
            }
            for (int j = 0; j < 3; j++) {
                split[i][j] = Integer.parseInt(l[i].split("\\.")[j]);
            }
        }
        Arrays.sort(split, comp);

        for (int i = 0; i < split.length; i++) {
            split[i] = Arrays.stream(split[i]).filter(x -> x != -1).toArray();
            out[i] = "";
            for (int v : split[i]) {
                out[i] += Integer.toString(v) + ".";
            }
            out[i] = out[i].substring(0, out[i].length() - 1);
        }
        return out;
    }

    public static void main(String[] args) {
        // String[] t = { "1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2" };
        String[] t = { "1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0" };
        System.out.println(Arrays.toString(solution(t)));
    }
}