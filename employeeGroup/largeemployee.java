package src.employeeGroup;

public class largeemployee extends employee {
    protected byte[] someData;
    public largeemployee(byte[] someData) {
        this.someData = someData;
    }

    public byte[] getSomeData() {
        return someData;
    }

    public void setSomeData(byte[] someData) {
        this.someData = someData;
    }
}