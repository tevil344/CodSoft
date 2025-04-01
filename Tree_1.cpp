#include<iostream>
#include<queue>
#include<string>
using namespace std;

class node{
    public:
        int data;
        node* left;
        node* right;
        node(int val){
            data=val;
            left=NULL;
            right=NULL;
        }
};

node* buildTree(node* root){
    if(root==NULL){
        int data;
        cout<<"Enter the data: ";
        cin>>data;
        root=new node(data);
    }
    cout<<"Enter the left child of "<<root->data<<": ";
    int leftData;
    cin>>leftData;
    if(leftData!=-1){
        root->left=buildTree(root->left);
    }
    cout<<"Enter the right child of "<<root->data<<": ";
    int rightData;
    cin>>rightData;
    if(rightData!=-1){
        root->right=buildTree(root->right);
    }
    return root;
}

int main(){
    node* root=NULL;
    root=buildTree(root);
    cout<<"Tree built successfully!"<<endl;
    return 0;
}