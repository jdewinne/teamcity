# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.investigations import Investigations  # noqa: F401,E501
# from dohq_teamcity.models.mutes import Mutes  # noqa: F401,E501
# from dohq_teamcity.models.problem_occurrences import ProblemOccurrences  # noqa: F401,E501


class Problem(TeamCityObject):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'href': 'str',
        'id': 'str',
        'identity': 'str',
        'investigations': 'Investigations',
        'mutes': 'Mutes',
        'problem_occurrences': 'ProblemOccurrences',
        'type': 'str'
    }

    attribute_map = {
        'href': 'href',
        'id': 'id',
        'identity': 'identity',
        'investigations': 'investigations',
        'mutes': 'mutes',
        'problem_occurrences': 'problemOccurrences',
        'type': 'type'
    }

    def __init__(self, href=None, id=None, identity=None, investigations=None, mutes=None, problem_occurrences=None, type=None, teamcity=None):  # noqa: E501
        """Problem - a model defined in Swagger"""  # noqa: E501

        self._href = None
        self._id = None
        self._identity = None
        self._investigations = None
        self._mutes = None
        self._problem_occurrences = None
        self._type = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        if identity is not None:
            self.identity = identity
        if investigations is not None:
            self.investigations = investigations
        if mutes is not None:
            self.mutes = mutes
        if problem_occurrences is not None:
            self.problem_occurrences = problem_occurrences
        if type is not None:
            self.type = type
        super(Problem, self).__init__(teamcity=teamcity)

    @property
    def href(self):
        """Gets the href of this Problem.  # noqa: E501


        :return: The href of this Problem.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Problem.


        :param href: The href of this Problem.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this Problem.  # noqa: E501


        :return: The id of this Problem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Problem.


        :param id: The id of this Problem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def identity(self):
        """Gets the identity of this Problem.  # noqa: E501


        :return: The identity of this Problem.  # noqa: E501
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this Problem.


        :param identity: The identity of this Problem.  # noqa: E501
        :type: str
        """

        self._identity = identity

    @property
    def investigations(self):
        """Gets the investigations of this Problem.  # noqa: E501


        :return: The investigations of this Problem.  # noqa: E501
        :rtype: Investigations
        """
        return self._investigations

    @investigations.setter
    def investigations(self, investigations):
        """Sets the investigations of this Problem.


        :param investigations: The investigations of this Problem.  # noqa: E501
        :type: Investigations
        """

        self._investigations = investigations

    @property
    def mutes(self):
        """Gets the mutes of this Problem.  # noqa: E501


        :return: The mutes of this Problem.  # noqa: E501
        :rtype: Mutes
        """
        return self._mutes

    @mutes.setter
    def mutes(self, mutes):
        """Sets the mutes of this Problem.


        :param mutes: The mutes of this Problem.  # noqa: E501
        :type: Mutes
        """

        self._mutes = mutes

    @property
    def problem_occurrences(self):
        """Gets the problem_occurrences of this Problem.  # noqa: E501


        :return: The problem_occurrences of this Problem.  # noqa: E501
        :rtype: ProblemOccurrences
        """
        return self._problem_occurrences

    @problem_occurrences.setter
    def problem_occurrences(self, problem_occurrences):
        """Sets the problem_occurrences of this Problem.


        :param problem_occurrences: The problem_occurrences of this Problem.  # noqa: E501
        :type: ProblemOccurrences
        """

        self._problem_occurrences = problem_occurrences

    @property
    def type(self):
        """Gets the type of this Problem.  # noqa: E501


        :return: The type of this Problem.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Problem.


        :param type: The type of this Problem.  # noqa: E501
        :type: str
        """

        self._type = type

