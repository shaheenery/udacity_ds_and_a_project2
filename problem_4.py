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
        if user is None or group is None:
            return "Please enter a valid user and group"

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

# Test 1 - A user is in a subgroup of the searched group

print(Group.is_user_in_group(sub_child_user, parent))
# True

# Test 2 - User does not exist group or any subgroup
print(Group.is_user_in_group("frank", parent))
# False

# Test 3 - There is only one group with no users and no subgroups
empty = Group("empty")
print(Group.is_user_in_group("frank", empty))
# False

# Test 4 - Null group
print(Group.is_user_in_group("frank", None))
# Please enter a valid user and group

# Test 5 - Null user
print(Group.is_user_in_group(None, empty))
# Please enter a valid user and group
