public class Node {
    private String data;
    private Node next;

    public Node(String data) {
        this.data = data;
    }

    public void setNext(Node node) {
        next = node;
    }

    public Node getNext() {
        return next;
    }

    public String getData() {
        return data;
    }
}
