pragma solidity >=0.7.0 < 0.8.0;

contract Asset{

    uint price;
    string name;

    function asset_() public {
        price = 5000;
        name = "computer";
    }

    function setter(uint _price, string memory _name) public{
        price = _price;
        name = _name;
    }

    function display() public view returns(string memory, uint){
        return (name, price);
    }

}