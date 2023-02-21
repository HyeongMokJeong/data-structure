import java.lang.Math;

public class HashMap {

    private int size = 10;
    private int test_data_size = 28;
    public Node[] list = new Node[size];

    public int hash(Node node) {
        return Math.abs(node.getData().hashCode() % (size));
    }

    public void add(Node node) {
        int hash = hash(node);

        if (list[hash] == null) {
            list[hash] = node;
        }
        else {
            Node target = list[hash];
            while (target.getNext() != null) {
                target = target.getNext();
            }
            target.setNext(node);
        }
    }

    public void show() {
        int i;
        for (i = 0; i < size; i++) {
            Node temp = list[i];
            System.out.print(i + "번째 데이터 : " + temp.getData());
            while (temp.getNext() != null) {
                temp = temp.getNext();
                System.out.print(" - " + temp.getData());
            }
            System.out.println();
        }
    }

    public Node search(String key) {
        int k = Math.abs(key.hashCode() % size);
        Node target = list[k];
        while (target != null) {
            if (target.getData().equals(key)) {
                return target;
            }
            target = target.getNext();
        }
        return null;
    }

    public static void main(String[] args) {
        HashMap hashMap = new HashMap();
        int i;
        for (i = 0; i < hashMap.test_data_size; i ++) {
            hashMap.add(new Node("testdata" + i));
        }
        hashMap.show();
        System.out.println(hashMap.search("testdata18").getData());
    }
}
