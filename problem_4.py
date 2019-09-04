# Active Directory

# In Windows Active Directory, a group can consist of user(s) and group(s)
# themselves. We can construct this hierarchy as such. Where User is
# represented by str representing their ids.

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    @classmethod
    def is_user_in_group(_cls, user, group):
        """
        Return True if user is in the group, False otherwise.

        Args:
          user(str): user name/id
          group(class:Group): group to check user membership against
        """
        if user in group.get_users():
            return True
        else:
            for sub_group in group.get_groups():
                if Group.is_user_in_group(user, sub_group):
                    return True

        return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(Group.is_user_in_group(sub_child_user, parent))
# True

print(Group.is_user_in_group("frank", parent))
# False

empty = Group("empty")
print(Group.is_user_in_group("frank", empty))
# False
