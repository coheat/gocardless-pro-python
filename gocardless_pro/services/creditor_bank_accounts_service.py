# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources

class CreditorBankAccountsService(base_service.BaseService):
    """Service class that provides access to the creditor_bank_accounts
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.CreditorBankAccount
    RESOURCE_NAME = 'creditor_bank_accounts'

    def create(self, params=None):
        """Create a creditor bank account.

        Creates a new creditor bank account object.

        Args:
          params (dict, optional): Request body.

        Returns:
          CreditorBankAccount
        """
        path = '/creditor_bank_accounts'
        response = self._perform_request('POST', path, params)
        return self._resource_for(response)

    def list(self, params=None):
        """List creditor bank accounts.

        Returns a [cursor-paginated](#overview-cursor-pagination) list of your
        creditor bank accounts.

        Args:
          params (dict, optional): Query string parameters.

        Returns:
          ListResponse of CreditorBankAccount instances
        """
        path = '/creditor_bank_accounts'
        response = self._perform_request('GET', path, params)
        return self._resource_for(response)

    def get(self, identity, params=None):
        """Get a single creditor bank account.

        Retrieves the details of an existing creditor bank account.

        Args:
          identity (string): Unique identifier, beginning with "BA".
          params (dict, optional): Query string parameters.

        Returns:
          CreditorBankAccount
        """
        path = self._sub_url_params('/creditor_bank_accounts/:identity', {
            'identity': identity,
        })
        response = self._perform_request('GET', path, params)
        return self._resource_for(response)

    def disable(self, identity, params=None):
        """Disable a creditor bank account.

        Immediately disables the bank account, no money can be paid out to a
        disabled account.
        
        This will return a `disable_failed`
        error if the bank account has already been disabled.
        
        A
        disabled bank account can be re-enabled by creating a new bank account
        resource with the same details.

        Args:
          identity (string): Unique identifier, beginning with "BA".
          params (dict, optional): Request body.

        Returns:
          CreditorBankAccount
        """
        path = self._sub_url_params('/creditor_bank_accounts/:identity/actions/disable', {
            'identity': identity,
        })
        response = self._perform_request('POST', path, params)
        return self._resource_for(response)

