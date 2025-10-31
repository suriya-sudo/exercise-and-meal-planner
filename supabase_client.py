import os
import streamlit as st
from typing import Optional
from supabase import create_client, Client


def get_supabase() -> Client:
    """Return a cached Supabase client initialized from Streamlit secrets or environment.

    Expected secrets/env:
      - SUPABASE_URL
      - SUPABASE_ANON_KEY
    """
    if "_supabase_client" in st.session_state and st.session_state._supabase_client is not None:
        return st.session_state._supabase_client  # type: ignore[attr-defined]

    url: Optional[str] = None
    key: Optional[str] = None

    # Prefer Streamlit secrets for deployment safety
    if hasattr(st, "secrets") and "SUPABASE_URL" in st.secrets and "SUPABASE_ANON_KEY" in st.secrets:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_ANON_KEY"]
    else:
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_ANON_KEY")

    if not url or not key:
        raise RuntimeError("Supabase credentials missing. Set SUPABASE_URL and SUPABASE_ANON_KEY in st.secrets or env.")

    client = create_client(url, key)
    st.session_state._supabase_client = client  # type: ignore[attr-defined]
    return client


