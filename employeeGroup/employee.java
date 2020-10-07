package src.employeeGroup;

public class employee {
    private int id;
    private String firstName;
    private String lastName;
    private int hireYear;

    public employee(int id, String firstName, String lastName, int hireYear) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.hireYear = hireYear;
    }

    public employee(){

    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public int getHireYear() {
        return hireYear;
    }

    public void setHireYear(int hireYear) {
        this.hireYear = hireYear;
    }

    @Override
    public String toString() {
        return "employee{" +
                "id=" + id +
                ", firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", hireYear=" + hireYear +
                '}';
    }
}
